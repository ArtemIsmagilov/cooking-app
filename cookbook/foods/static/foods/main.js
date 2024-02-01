async function get_endpoint() {
    let response = await fetch('/api/v1/show_recipes_without_product/1/');
    let result = await response.json();
    let table = ''
    for (let i = 0; i < result.length; i++) {
        let value = result[i]
        table = table.concat(`<tr><th scope="row">${value.recipe_id}</th><th>${value.title}</th></tr>`);
    }
    document.getElementById("recipe_table").innerHTML = table
}
