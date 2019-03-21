new Chart(document.getElementById("bar-chart"), {
    type: 'horizontalBar',
    data: {
    labels: p_chave_label,
    datasets: [
        {
        label: "Frequência da Palavra-Chave",
        backgroundColor: ["#4900E5", "#4119E5","#3A32E6","#334BE7","#2B64E8","#247DE9","#1D96EA","#15AFEB","#0EC8EC","#07E1ED"],
        data: p_chave_valor
        }
    ]
    },
    options: {
        legend: { display: false },
        title: {
            display: true,
            text: ''
        },
        scales: {
            xAxes: [{
                ticks: {
                    min : 0
                }
            }],
            yAxes: [{
                ticks: {
                    fontSize: 15
                }
            }]
        }
    }
});

new Chart(document.getElementById("line-chart"), {
    type: 'line',
    data: {
    labels: p_anos_ano,
    datasets: [
        {
        label: "Frequência da Palavra-Chave",
        data: p_anos_valor
        }
    ]
    },
    options: {
        legend: { display: false },
        title: {
            display: true,
            text: ''
        },
        scales: {
            xAxes: [{
                ticks: {
                    min : 0
                }
            }],
            yAxes: [{
                ticks: {
                    fontSize: 15
                }
            }]
        }
    }
});