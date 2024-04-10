document.addEventListener("DOMContentLoaded", function() {



var dataAtual = new Date();
var mesesEmPortugues = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    ] 

var mes_atual = dataAtual.getMonth()
var ano_atual = dataAtual.getFullYear()
var inicioAnoLetivo = obterAnoLetivo(mes_atual,ano_atual)
var select_mes = document.getElementById('mes')

var select_ano = document.getElementById('ano')
var mes_atual_portugues = mesesEmPortugues[mes_atual]
select_mes.value = mes_atual_portugues

select_ano.value = inicioAnoLetivo

 
localStorage.setItem('select_mes',mes_atual_portugues)
localStorage.setItem('select_ano', inicioAnoLetivo)
  
  
  
}) 
  
  
  
  // Função para obter o valor de um cookie pelo nome

  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Verifique se este cookie é o cookie de token CSRF
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Função para atualizar o estado do checkbox
function atualizarMensalidade(mensalidadeId) {
    var checkbox = document.getElementById('paga-' + mensalidadeId);
    if (checkbox) {
        var paga = checkbox.checked;

        // Obtenha o token CSRF do cookie
        var csrfToken = getCookie('csrftoken');
        if (csrfToken) { // Verifique se o token CSRF está definido
            // Crie uma instância de XMLHttpRequest
            var xhr = new XMLHttpRequest();
            xhr.open('POST', '/escolas/atualizarMensalidadeAluno/' + mensalidadeId + '/');
            xhr.setRequestHeader('Content-Type', 'application/json');
            xhr.setRequestHeader('X-CSRFToken', csrfToken); // Adicione o token CSRF ao cabeçalho

            // Defina a função de tratamento do evento onload
            xhr.onload = function() {
                if (xhr.status === 200) {
                    console.log('Mensalidade atualizada com sucesso!');
                } else {
                    console.error('Erro ao atualizar a mensalidade:', xhr.statusText);
                }
            };

            // Envie a solicitação com os dados JSON
            xhr.send(JSON.stringify({ paga: paga }));
        } else {
            console.error('Token CSRF não encontrado.');
        }
    } else {
        console.error('Elemento do checkbox não encontrado.');
    }
}

function salvarValorSelecionado(){
    var select_ano = document.getElementById('ano')
    var select_mes = document.getElementById('mes')
    
    var valor_selecionado_mes = select_mes.value
    var valor_selecionado_ano  = select_ano.value


    localStorage.setItem('valor_selecionado_mes', valor_selecionado_mes)
    localStorage.setItem('valor_selecionado_ano', valor_selecionado_ano)
    
}

window.onload = function(){
    var valor_salvo_mes = localStorage.getItem('valor_selecionado_mes')
    var valor_salvo_ano = localStorage.getItem('valor_selecionado_ano')
    console.log(valor_salvo_ano)

    if (valor_salvo_mes){
        var select_mes = document.getElementById('mes')
        select_mes.value = valor_salvo_mes
    }
    if (valor_salvo_ano){
        var select_ano = document.getElementById('ano')
        select_ano.value = valor_salvo_ano
    }
}




function obterAnoLetivo(mes, ano){
    if (mes < 8){
        return ano -= 1
    }else {
        return ano
    }
}


