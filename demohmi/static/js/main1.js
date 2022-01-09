//var socket =new WebSocket('ws://localhost:8000/ws/demohmi/');
var socket =new WebSocket('ws://rony.pythonanywhere.com/ws/demohmi/');

socket.onmessage = function(e){
    var djangoData = JSON.parse(e.data);
    //console.log(djangoData);
    document.querySelector('#hora').innerText = djangoData.HORA;
    document.querySelector('#corriente').innerText = djangoData.CORRIENTE;
    document.querySelector('#voltaje').innerText = djangoData.VOLTAJE;
    document.querySelector('#potenciakw').innerText = djangoData.POTENCIA_KW;
    document.querySelector('#frecuencia').innerText = djangoData.FRECUENCIA;
    document.querySelector('#potencia').innerText = djangoData.POTENCIA;
    document.querySelector('#velocidad').innerText = djangoData.VELOCIDAD;
    document.querySelector('#temperatura').innerText = djangoData.TEMPERATURA;
    document.querySelector('#nivel').innerText = djangoData.NIVEL;
    document.querySelector('#presion').innerText = djangoData.PRESION ;
    document.querySelector('#caudal').innerText = djangoData.CAUDAL;
    document.querySelector('#acumulado').innerText = djangoData.ACUMULADO;
}