var host = window.location.protocol + "//" + window.location.host + "/wines/";

async function send_options(data) {
    console.log(`${host}`)

    const response = await fetch(`${host}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json;charset=utf-8'
        },
        body: JSON.stringify(data)
    });
}
