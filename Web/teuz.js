//variável predefinada da dpi do teuzz
window.dpipadrao3 = 800

function calcularValores3() {
    var valor5 = parseFloat(document.getElementById('input1').value);
    var valor6 = parseFloat(document.getElementById('input2').value);
}

    // Verificar se os valores são válidos
    if (isNaN(valor5) || isNaN(valor6)) {
        alert('Por favor, insira um número válido.');
        return; 

    //Calcular resultados
    var resultado = (dpipadrao3 * valor6) * valor5;
        // Exibe o resultado
        document.getElementById('input3').value = resultado.toFixed(2); // Arredondar para duas casas decimais
    }
    
    window.onload = function() {
        document.getElementById('btn_calc').addEventListener('click', function(event) {
          event.preventDefault();
          calcularValores3();
        });
      }