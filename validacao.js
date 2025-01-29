import joi from 'joi';
 
export const modeloCarro = joi.object({
        nome: joi.string().min(3).required().mensagem({'string.min': 'O nome do carro deve ter pelo menos 3 caracteres.', 'any.required': 'O nome do carro é obrigatório.'
}),
        sigla: joi.string().length(3).required().mensagem({'string.length': 'A sigla do carro deve ter 3 caracteres.', 'any.required': 'A sigla do carro é obrigatório., any.required': 'O nome do carro é obrigatório.'
}),
        velocidadeMaxima: joi.number().min(1).required().mensagem({'number.min': 'A velocidade maxima minima é 1km/h.', 'any.required': 'A velocidade maxima do carro é obrigatório.'
}),        
        potencia: joi.number().min(1).required().message({'number.min': 'A potência minima é 1 Cv.', 'any.required': 'A potência do carro é obrigatório.. any.required': 'O nome do carro é obrigatório.'
}),
        consumo: joi.number().min(0.1).required().mensagem({'number.min': 'O consumo minimo é 0.1 l/100km.', 'any.required': 'O consumo do carro é obrigatório.'
})

});

 
 
// Validação para atualização de carro.
export const modeloAtualizacaoCarro = joi.object({
        nome: joi.string().min(3), // Nome do carro, pelo menos 3 caracteres
        sigla: joi.string().length(3),  // Sigla ou modelo, 3 caracteres
        velocidadeMaxima: joi.number().min(1),  // Potência minima é 1 Cv
        potencia: joi.number().min(1),  // Velocidade miníma de 1km/h
        consumo: joi.number().min(0.1), // Ano de fabricação
})