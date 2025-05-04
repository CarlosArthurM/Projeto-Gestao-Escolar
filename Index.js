const venom = require('venom-bot');

// Objeto para guardar temporariamente os dados
const dadosTemporarios = {};

venom.create({ session: 'bot-escola' })
  .then((client) => {
    client.onMessage(async (message) => {
      const telefone = message.from;
      const msg = message.body.toLowerCase();

      // Se tiver dados temporários, está no meio de uma coleta
      if (dadosTemporarios[telefone]) {
        if (!dadosTemporarios[telefone].serie) {
          // Guarda a série e pede a turma
          dadosTemporarios[telefone].serie = message.body;
          await client.sendText(telefone, 'Agora informe sua turma:');
          return;
        } else {
          // Guarda a turma e processa os dados
          const turma = message.body;
          const serie = dadosTemporarios[telefone].serie;
          
          // Aqui você pode fazer o que quiser com os dados
          console.log('Dados coletados:', { telefone, serie, turma });
          
          await client.sendText(telefone, `✔️ Anotado!\nSérie: ${serie}\nTurma: ${turma}`);
          delete dadosTemporarios[telefone]; // Limpa os dados
          return;
        }
      }

      // Menu principal com switch
      switch(msg) {

        case 'menu':
          await client.sendText(telefone, '📋 MENU:\n1. Documentos\n2. Horários');
          break;

        case '1':
          await client.sendText(telefone, 'Preencha o formulario: ');
          break;

        case '2':
          dadosTemporarios[telefone] = {}; // Prepara para coletar dados
          await client.sendText(telefone, 'Para ver horários, informe sua série:');
          break;

        default:
          await client.sendText(telefone, `Olá, eu sou o bot da Escola e estou aqui para te ajudar, digite "menu" para ver as opções.`);
      }
    });
  })
  .catch((erro) => {
    console.log('Erro ao iniciar o bot:', erro);
  });