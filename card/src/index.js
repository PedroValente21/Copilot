function getCardBrand(cardNumber) {
    const brands = {
        visa: /^4[0-9]{12}(?:[0-9]{3})?$/,
        mastercard: /^(2[2-7]|5[1-5])[0-9]{14}$/,
        amex: /^3[47][0-9]{13}$/,
        discover: /^6(?:011|5[0-9]{2})[0-9]{12}$/,
        hipercard: /^6062[0-9]{12}$/,
        // Adiocione um JCB, Diners Club, Discover, EnRoute, Voyager, Hipercard e Aura
        jcb: /^(?:2131|1800|35\d{3})\d{11}$/,
        diners: /^3(?:0[0-5]|[68][0-9])[0-9]{11}$/,
        enroute: /^(2014|2149)\d{11}$/,
        voyager: /^8699\d{11}$/,
        aura: /^50[0-9]{14}$/,
    };

    for (const brand in brands) {
        if (brands[brand].test(cardNumber)) {
            return brand;
        }
    }

    return 'unknown';
}

// Exemplo de uso:
const cardNumber = '4111111111111111'; // Substitua pelo número real do cartão
console.log(getCardBrand(cardNumber));