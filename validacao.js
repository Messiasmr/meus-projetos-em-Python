import joi from 'joi';
 
export const modeloCarro = joi.object({
        nome: joi.string().min(3).required(),
        sigla: joi.string().length(3).required(),
        velocidadeMaxima: joi.number().min(1).required(),
        potencia: joi.number().min(1).required(),
        consumo: joi.number().min(0.1).required(),
});
 
 
// Validação para atualização de carro.
export const modeloAtualizacaoCarro = joi.object({
        nome: joi.string().min(3), // Nome do carro, pelo menos 3 caracteres
        sigla: joi.string().length(3),  // Sigla ou modelo, 3 caracteres
        velocidadeMaxima: joi.number().min(1),  // Potência minima é 1 Cv
        potencia: joi.number().min(1),  // Velocidade miníma de 1km/h
        consumo: joi.number().min(0.1), // Ano de fabricação
})