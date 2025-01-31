//variavel predefinida do dpi do lulu
window.dpipadrao2 = 400;

function calcularValores2() {
    var valor3 = parseFloat(document.getElementById('input1').value);
    var valor4 = parseFloat(document.getElementById('input2').value);

    // Verificar se os valores são válidos
    if (isNaN(valor3) || isNaN(valor4)) {
        alert('Por favor, insira um número válido.');
        return; 
    }

    // Realiza o cálculo
    var resultado = (dpipadrao2 * valor4) / valor3;

    // Exibe o resultado
    document.getElementById('input3').value = resultado.toFixed(2); // Arredondar para duas casas decimais
}

// Esperar o DOM ser carregado e adicionar o evento de clique no botão
window.addEventListener('DOMContentLoaded', function() {
    document.getElementById('btn_calc').addEventListener('click', function(event) {
        event.preventDefault(); // Previne o comportamento padrão do botão
        calcularValores2(); // Chama a função de cálculo
    });
});
