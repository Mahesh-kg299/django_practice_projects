let getCSRFToken = () => {
    let cookies = document.cookie.split(";")
    let csrftoken = ""
    for (let cookie of cookies) {
        let [key, value] = cookie.split("=")
        if (key = 'csrftoken') {
            csrftoken = value
        }
    }
    return csrftoken
}

let sendData = async (url, data) => {
    let response = await fetch(url, {
        method: "POST",
        body: data,
        headers: {
            'X-CSRFToken': getCSRFToken()
        }
    })
    let jsonData = await response.json()
    return jsonData
}

let getFormatedeValue = (value) => {
    if(value == 'inf'){
        return 'Infinity'
    }
    let [mantissa, exponent] = value.split('e')
    let fromatedValue = `${mantissa}&times10<sup>${exponent}</sup>`
    return fromatedValue
}