const venom = require('venom-bot');

// Objeto para guardar temporariamente os dados
const dadosTemporarios = {};

venom.create({ session: 'bot-escola' })
  .then((client) => {
    client.onMessage(async (message) => {
      const telefone = message.from;
      const msg = message.body.toLowerCase();

      // verifica se tá coletando dado
      if (dadosTemporarios[telefone]) {
        // verifica se escolheu opcao doumento
        if (dadosTemporarios[telefone].opcao === "documento") {
          // verifica se não coletou o nome ainda
          if (!dadosTemporarios[telefone].nome) {
            dadosTemporarios[telefone].nome = message.body;
            await client.sendText(telefone, "Informe sua data de nascimento");
            return;

          } else if (!dadosTemporarios[telefone].dataNascimento) {
            dadosTemporarios[telefone].dataNascimento = message.body;
            await client.sendText(telefone, "Informe o documento que deseja pedir");
            return;

          } else {
            dadosTemporarios[telefone].tipoDoc = message.body;
            console.log(dadosTemporarios[telefone]);
            await client.sendText(telefone, "Documento solicitado com sucesso!");
            delete dadosTemporarios[telefone];
            return;
          }
        }
        
        if (dadosTemporarios[telefone].opcao === "horario") {
          if (!dadosTemporarios[telefone].turma) {
            dadosTemporarios[telefone].turma = message.body;
            await client.sendText(telefone, "Informe sua série");
            return;
            
          } else {
            dadosTemporarios[telefone].serie = message.body;
            console.log(dadosTemporarios[telefone]);
            await client.sendText(telefone, "Horário solicitado com sucesso!");
            delete dadosTemporarios[telefone];
            return;
          }
        
        }

        if(dadosTemporarios[telefone].opcao === "transferir"){
          if (!dadosTemporarios[telefone].nome) {
            dadosTemporarios[telefone].nome = message.body;
            await client.sendText(telefone, "Informe turma");
            return;
            
          } else {
            dadosTemporarios[telefone].serie = message.body;
            console.log(dadosTemporarios[telefone]);
            await client.sendText(telefone, `${dadosTemporarios[telefone].nome.split(' ')[0]} vamos redirecionar você ao setor responsável `);
            delete dadosTemporarios[telefone];
            return;
          }
        }
      }

      // Menu principal com switch
      switch(msg) {
        case 'menu':
          await client.sendText(telefone, '📋 MENU:\n1. Solicitar Documento(Comprovante de Matricula, Atestado de frequência e etc..)\n2. Solicitar Horários\n3. Solicitar Cardápio\n4. O que eu preciso para mudar de turma ou de turno?\n5. tem reforço ou aula extra para quem está com dificuldade?\n6. O uniforme é obrigatório todos os dias? E se eu esquecer?\n7. Solicitar Boletim\n8. Vou mudar de cidade, como transfiro minha matrícula?');
          break;

        case '1':
          dadosTemporarios[telefone] = { opcao: "documento" };
          await client.sendText(telefone, "Informe seu nome completo");
          break;

        case '2':
          dadosTemporarios[telefone] = { opcao: "horario" };
          await client.sendText(telefone, "Informe sua turma");
          break;
        
        case '3':
          //enviar o cardapio usando json e banco de dados
          break;
        
        case '4':
          dadosTemporarios[telefone] = { opcao: "trocar_turma" };
          break;
        
        case '5':
          await client.sendText(telefone, "Sim-sugerir msterias, vídeo-aulas.");
          break;

        case '6':
          await client.sendText(telefone, "Sim, deverá justificar ao responsável ");
          break;

        case '7':
          await client.sendText(telefone, "Sim, deverá justificar ao responsável ");
          break;

        case '8':
          dadosTemporarios[telefone] = { opcao: "transferir" };
          await client.sendText(telefone, "Informe seu nome completo");
          break;

        default:
          await client.sendText(telefone, `Olá, eu sou o bot da Escola e estou aqui para ajudar você, digite "menu" para ver as opções.`);
      }
    });
  })
  .catch((erro) => {
    console.log('Erro ao iniciar o bot:', erro);
  });