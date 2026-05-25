// SHOW MODULE

function showModule(moduleId){

    let modules = document.querySelectorAll('.module');

    modules.forEach(module => {
        module.classList.remove('active');
    });

    document.getElementById(moduleId).classList.add('active');
}

function changeTestingMethod(value){

    if(value !== ''){
        showModule(value);
    }
}

// LOADING EFFECT

function showLoading(elementId){

    document.getElementById(elementId).innerHTML =
    "Scanning Target...";
}

// PORT SCANNER

async function scanPorts(){

    showLoading('portResult');

    let target = document.getElementById('target').value;

    let response = await fetch('/portscan',{

        method:'POST',

        headers:{
            'Content-Type':'application/json'
        },

        body:JSON.stringify({
            target:target
        })

    });

    let data = await response.json();

    document.getElementById('portResult').innerHTML =
    JSON.stringify(data,null,2);
}

// VULN SCANNER

async function scanVuln(){

    showLoading('vulnResult');

    let url = document.getElementById('url').value;

    let response = await fetch('/vulnscan',{

        method:'POST',

        headers:{
            'Content-Type':'application/json'
        },

        body:JSON.stringify({
            url:url
        })

    });

    let data = await response.json();

    document.getElementById('vulnResult').innerHTML =
    JSON.stringify(data,null,2);
}

// PASSWORD CHECKER

async function checkPassword(){

    showLoading('passwordResult');

    let password = document.getElementById('password').value;

    let response = await fetch('/passwordcheck',{

        method:'POST',

        headers:{
            'Content-Type':'application/json'
        },

        body:JSON.stringify({
            password:password
        })

    });

    let data = await response.json();

    document.getElementById('passwordResult').innerHTML =
    JSON.stringify(data,null,2);
}

// OSINT

async function scanOSINT(){

    showLoading('osintResult');

    let domain = document.getElementById('domain').value;

    let response = await fetch('/osint',{

        method:'POST',

        headers:{
            'Content-Type':'application/json'
        },

        body:JSON.stringify({
            domain:domain
        })

    });

    let data = await response.json();

    document.getElementById('osintResult').innerHTML =
    JSON.stringify(data,null,2);
}