function calcularValores() {
    // Pegando os valores dos inputs e convertendo para números
    var valor1 = parseFloat(document.getElementById('input1').value);
    var valor2 = parseFloat(document.getElementById('input2').value);

    // Verificar se os valores são válidos
    if (isNaN(valor1) || isNaN(valor2)) {
        alert('Por favor, insira um número válido.');
        return; // Parar a execução caso haja erro
    }

    // Realizando a soma
    var resultado = valor1 + valor2;

    // Definindo o valor do resultado no input3
    document.getElementById('input3').value = resultado;
}
