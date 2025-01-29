import carros2025 from './tabelacarros.js';
import express from 'express';
import { modeloCarro, modeloAtualizacaoCarro } from './validacao.js';

const app = express();
app.use(express.json());

app.get('/', function (_requisicao, resposta) {
    resposta.status(200).send(carros2025);
});

app.get('/:sigla', (req, res) => {
    const siglaInformada = req.params.sigla.toUpperCase();
    const carro = carros2025.find(
        (infoCarro) => infoCarro.sigla === siglaInformada
    );
    if (!carro) {
        res.status(404).send("Não existe carro com a sigla informada!");
        return;
    }
    res.status(200).send(carro);
});

app.post('/', (req, res) => {
    const novoCarro = req.body;
    const { error } = modeloCarro.validate(novoCarro);
    if (error) {
        res.status(400).send(error);
        return;
    }
    carros2025.push(novoCarro);
    res.status(200).send(novoCarro);
});

app.put('/:sigla', (req, res) => {
    const siglaInformada = req.params.sigla.toUpperCase();
    const carroSelecionado = carros2025.find((c) => c.sigla === siglaInformada);
    if (!carroSelecionado) {
        res.status(404).send("Não existe carro com a sigla informada");
        return;
    }
    const { error } = modeloAtualizacaoCarro.validate(req.body);
    if (error) {
        res.status(400).send(error);
        return;
    }
    const campos = Object.keys(req.body);
    for (let campo of campos) {
        carroSelecionado[campo] = req.body[campo];
    }
    res.status(200).send(carroSelecionado);
});

// Nova rota DELETE para excluir um carro com base na sigla
app.delete('/:sigla', (req, res) => {
    const siglaInformada = req.params.sigla.toUpperCase();
    const index = carros2025.findIndex((carro) => carro.sigla === siglaInformada);
    if (index !== -1) {
        carros2025.splice(index, 1);
        res.status(200).send({ message: `Carro com sigla ${siglaInformada} excluído com sucesso.` });
    } else {
        res.status(404).send({ message: `Carro com sigla ${siglaInformada} não encontrado.` });
    }
});

const PORTA = 3000;
app.listen(PORTA, () => {
    console.log(`Servidor rodando com sucesso na porta ${PORTA}`);
});
