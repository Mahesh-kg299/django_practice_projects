const sendRequest = async function (url, method, requestData = null, ele){
    let responce = null
    if(method == "GET"){
        responce = await fetch(url, {
            method: method,
            credentials: "same-origin"
        })
    }
    else{
        responce = await fetch(url, {
            method: method,
            body: requestData,
            credentials: "same-origin"
        })
    }
    let data = await responce.text()
    ele.innerHTML = data
}

const tableBody = document.querySelector("#dataTable tbody")

for(let i = 1; i <= 3; i++){
    const tr = document.createElement("tr")
    const td1 = document.createElement("td")
    const td2 = document.createElement("td")
    const keyInput = document.createElement("input")
    const valueInput = document.createElement("input")
    keyInput.type = "text"
    valueInput.type = "text"
    keyInput.name = "key" + i
    valueInput.name = "value" + i
    td1.appendChild(keyInput)
    td2.appendChild(valueInput)
    tr.appendChild(td1)
    tr.appendChild(td2)
    tableBody.appendChild(tr)
}

const submitForm = function (e){
    e.preventDefault()
    const form = document.querySelector("form")
    let data = new FormData()
    for(let i = 1; i <= 3; i++){
        data.append(form["key" + i].value, form["value" + i].value)
    }
    data.append("csrfmiddlewaretoken", form["csrfmiddlewaretoken"].value)
    let url = form["url"].value
    let ele = document.querySelector(".responce-container")
    let method = form["method"].value
    sendRequest(url, method, data, ele)
}