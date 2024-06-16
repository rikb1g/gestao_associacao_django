const total = document.querySelector("#total")


document.addEventListener("DOMContentLoaded", function(){
    const rows = document.querySelectorAll(".linhadados")

    rows.forEach((row, index) =>{
        const entradaElement = row.querySelector(".entrada");
        const despesaElement = row.querySelector(".despesa");
        const totalElement = row.querySelector(".total");

        if (entradaElement && despesaElement) {
            const entrada = parseFloat(entradaElement.innerText) || 0;
            const despesa = parseFloat(despesaElement.innerText) || 0;

            if (!isNaN(entrada) && !isNaN(despesa)) {
                const total = entrada - despesa;
                if (total <0 ){
                    totalElement.classList.add('vermelho')
                } else if (total >0){
                    totalElement.classList.add('verde')
                }
                totalElement.innerText = total.toFixed(2);
            } else {
                console.error(`Erro na conversão de valores na linha ${index + 1}`);
            }

            
        } 
        
        
    });

    })


