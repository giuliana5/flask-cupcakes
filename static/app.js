async function listCupcakes() {

    // retrieve list of cupcakes from api
    const res = await axios.get("/api/cupcakes");
    
    cupcakes = res.data.cupcakes;

    // iterate through cupcakes to list each one
    for (cupcake of cupcakes) {
        $("#cupcakes").append(cupcakeMarkup(cupcake));
    }
}

function cupcakeMarkup(cupcake) {

    return $(`
        <div class="cupcake" data-id="${cupcake.id}"/>
            <button class="delete">X</button>
            <img src=${cupcake.image} width="200px" height="250px"/>
            <p class="flavors">${cupcake.flavor}</p>
        </div>
    `)
}

async function addCupcake(evt) {
    evt.preventDefault();

    // set vars for each form value
    const flavor = $("#flavor").val().toLowerCase();
    const size = $("#size").val();
    const image = $("#image").val();
    const rating = $("#rating").val();

    // send post request to api for new cupcake
    const addCupcake = await axios.post("/api/cupcakes", {
        flavor,
        size,
        image,
        rating
    });

    // generate markup for the new cupcake
    const newCupcake = $(cupcakeMarkup(addCupcake.data.cupcake));
    $("#cupcakes").append(newCupcake);

    // reset form
    $("#add-cupcake-form").trigger("reset");

} 

$("#add-cupcake-form").on("submit", addCupcake)

async function deleteCupcake() {

    // identify the id
    const id = $(this).parent().data("id")

    // delete cupcake from api
    await axios.delete(`/api/cupcakes/${id}`);

    // remove cupcake div from homepage
    $(this).parent().remove();
}

$("#cupcakes").on("click", ".delete", deleteCupcake);

listCupcakes();
