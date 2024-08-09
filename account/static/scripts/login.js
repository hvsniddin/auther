const form = document.querySelector('form');
const username = document.querySelector('input[name="username"]');
const password = document.querySelector('input[name="password"]');
const error = document.querySelector('p.error');

form.onsubmit = async (event) => {
    event.preventDefault();

    const url = new URL(window.location.href);
    const requestedDashboard = url.searchParams.get('requested');
    console.log(requestedDashboard);

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
    console.log(data);

    if (!data.ott) return;
    if (requestedDashboard!==data.dashboard) {
        error.style.display = 'block';
        form.dataset.submitting = "false";
        return
    }
    
    window.location.replace(`http://${requestedDashboard ? requestedDashboard : data.dashboard}.thewolfanalytics.uz/?ott=${data.ott}`)
}
