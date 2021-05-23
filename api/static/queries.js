import { parseForm } from "../js-form-parser/src/index.js";
function Queries() {
    const BASE = "http://127.0.0.1:5000/"
    let submit_button = document.getElementById('queries-submit');
    submit_button.onclick = async () => {
        const form = document.getElementById("queries-form");
        const fields = parseForm(form);
        
        await fetch("http://127.0.0.1:5000/edit/bed?description=1331", {
            method: 'put',
        })

        console.log(fields);
        console.log(12);
        alert(13)
    }
}
console.log(12)
Queries()