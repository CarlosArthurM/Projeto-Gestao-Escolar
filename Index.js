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
      }

      // Menu principal com switch
      switch(msg) {
        case 'menu':
          await client.sendText(telefone, '📋 MENU:\n1. Solicitar Documento\n2. Solicitar Horários\n3. Solicitar Cardápio');
          break;

        case '1':
          dadosTemporarios[telefone] = { opcao: "documento" };
          await client.sendText(telefone, "Informe seu nome completo");
          break;

        case '2':
          dadosTemporarios[telefone] = { opcao: "horario" };
          await client.sendText(telefone, "Informe sua turma");
          break;

        default:
          await client.sendText(telefone, `Olá, eu sou o bot da Escola e estou aqui para te ajudar, digite "menu" para ver as opções.`);
      }
    });
  })
  .catch((erro) => {
    console.log('Erro ao iniciar o bot:', erro);
  });