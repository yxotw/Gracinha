//variavel predefinida do dpi do black
window.dpipadrao = 6400;

function calcularValores() {
    var valor1 = parseFloat(document.getElementById('input1').value);
    var valor2 = parseFloat(document.getElementById('input2').value);

    if (isNaN(valor1) || isNaN(valor2)) {
        alert('Por favor, insira um número válido.');
        return; 
    }

    var resultado = (dpipadrao * valor2) / valor1;

    document.getElementById('input3').value = resultado.toFixed(2);
  }

  window.onload = function() {
    document.getElementById('btn_calc').addEventListener('click', function(event) {
      event.preventDefault();
      calcularValores();
    });
  }

  
