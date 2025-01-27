import carros2025 from "./tabelacarros.js"; //
// Importa o módulo "Express" um framework para construção de aplicativos de web em node.js
import express from 'express';

import { modeloCarro, modeloAtualizacaoCarro } from "./validacao.js"

// 
const app = express();

// Configura o express para entender requisições com o corpo em formato JSON.
app.use(express.json());

// Define uma rota get no caminho '/' que irá retornar a lista completa de carros.
app.get('/', function (_requisicao, resposta) {
        // Quando a rota for acessada, a resposta terá o codigo de status 200 (ok) e enviara a lista de carros.
        resposta.status(200).send(carros2025); // Retorna lista de carros com status 200 (requisição bem-sucedida).
    });

app.get('/:sigla', (req, res) => {
    const siglaInformada = req.params.sigla.toUpperCase();  // Obtém a sigla e deixa Maíuscula
    const carro = carros2025.find(
        (infoCarro) => infoCarro.sigla === siglaInformada
    );  // Busca o carro pela silga.
    if (!carro) {
        // Se o carro não for encontrado retorna o erro 404.
        res.status(404).send("Não existe carro com a sigla informada!");
        return;
    }
    res.status(200).send(carro);   // Se encontrado retorna o carro e status 200.
});

// Define a porta do servidor
const PORTA = 3000;
app.listen(PORTA, () => {
    console.log(`Servidor rodando com sucesso na porta ${3000}`);
});

app.post('/', (req, res) => {
    const novoCarro = req.body; // Obtém o novo carro emviado no corpo da requisição.
    const { error } = modeloCarro.validate(novoCarro); // Válida os dados do novo Carro.
    if (error) {
        // Se houver erro de válidação, retorna o erro 400
        res.status(400).send(error);
        return;
    }
    carros2025.push(novoCarro); // Adiciona o carro a lista de carros.
    res.status(200).send(novoCarro);    // Retorna o carro adicionado com status 200.

});

app.put("/:sigla", (req, res) => {
    const siglaInformada = req.params.sigla.toUpperCase();
    const carroSelecionado = carros2025.find((c) => c.sigla === siglaInformada);
    if (!carroSAelecionado) {
        // Se o carro não for encontrado, retorna o erro 404
        res.status(404).send(" Não existe carro com a sigla informada");
        return;
    };
    // Válida os dados da requisição com o modelo da atualização:
    const { error } = modeloAtualizacaoCarro.validate(req.body);
    if (error) {
        // Se houver erro de válidação retorna o erro 400
        res.status(400).send(error);
        return;
    }
    const campos = Object.keys(req.body);
    for (let campo of campos) {
        carrosSelecionado[campo] = req.body[campo];
    }
    res.status(200).send(carroSelecionado);
});
// Comandos para executar o app
// node app.js Inicia o Node.js
// npm start ou app.js ou ./app.js - Inicia o server
// Iniciar server pelo nodemon
// Npx nodemon app.js npm nodemon