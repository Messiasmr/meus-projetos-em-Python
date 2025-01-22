import carros2025 from "./tabelaCarros.js";
import express from "express";

const app = express();

app.use(express.json())

app.get('/',(requisicao,resposta) => {
    resposta.status(200),send(carros2025);
});

app.listen(3001, () => {
    console.log("Servidor rodando na porta 3001");

});
