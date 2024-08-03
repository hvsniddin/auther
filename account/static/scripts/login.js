const form = document.querySelector('form');
const username = document.querySelector('input[name="username"]');
const password = document.querySelector('input[name="password"]');
const error = document.querySelector('p.error');

form.onsubmit = async (event) => {
    event.preventDefault();

    if (form.dataset.submitting=='true') return;
    form.dataset.submitting = 'true';
    error.style.display = 'none';

    const resp = await fetch('/token/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            username: username.value,
            password: password.value
        })
    });

    if (!resp.ok) {
        error.style.display = 'block';
        form.dataset.submitting = "false";
        return
    }

    const data = await resp.json();
    if (!data.ott) return;
    window.location.replace(`http://127.0.0.1:8001/?ott=${data.ott}`)
}
