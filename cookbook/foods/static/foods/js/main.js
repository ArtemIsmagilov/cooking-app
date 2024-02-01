'use strict';

document
    .getElementById('searching')
    .addEventListener('input', (e) => get_endpoint(e.target.value))

async function get_endpoint(recipe_id) {
    let table = ''

    if ( 0 < +recipe_id && +recipe_id < 999) {
        let response = await fetch(`/api/v1/show_recipes_without_product/${recipe_id}/`);
        let result = await response.json();
        for (let i = 0; i < result.length; i++) {
            let value = result[i]
            table = table.concat(`<tr><th scope="row">${value.recipe_id}</th><th>${value.title}</th></tr>`);
        }
    }

    document.getElementById("recipe_table").innerHTML = table
}
