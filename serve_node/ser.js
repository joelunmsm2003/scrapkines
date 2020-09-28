#!/usr/bin/env node

const axios = require('axios');

const socket = require('socket.io-client')('https://sexy.estrellita.space:3003');
const someDelay = 10;
socket.on('connect', function () {
    console.log('connected...');
    if (process.argv[2] && process.argv[3]) {
        console.log('sending ' + process.argv[2] + ': ' + process.argv[3]);
        socket.emit(process.argv[2], process.argv[3]);
        setTimeout(() => {
            process.exit(0);  
        }, someDelay);
    } else {
        console.log('usage: ./client.js <event> <data>');

        

        axios.get(url).then((response)=>{
        if (response.status >= 400) {
            console.log(response.status);
            throw new Error("Bad response from server");
        } else{
            return response.data
        }
        }).then((data)=>{

        console.log('Enviando datos')

        socket.emit('send_message',{user: 'socket.username', event: 'left'});

        })

       
    }
});