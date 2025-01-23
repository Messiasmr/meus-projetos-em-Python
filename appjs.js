import carros2025 from "./tabelaCarros.js";
import express from "express";

const app = express();

app.use(express.json())

app.get('/',(requisicao,resposta) => {
    resposta.status(200).send(carros2025);
});

app.get("/:sigla",(req, res) => {
    const siglainformada = req.params.sigla.toUpperCase();
    const carro = carros2025.find(
        (infoCarro) => infoCarro.sigla === siglainformada
    );
    if(!carro){
        res.status(404).send('não existe carro com essa sigla');
        return;
    }
    res.status(200).send(carro);
    });


app.listen(3001, () => {
    console.log("Servidor rodando na porta 3001");

});
