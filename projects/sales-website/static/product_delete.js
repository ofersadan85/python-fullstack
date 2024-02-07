function deleteProduct(event) {
    let button = event.target;
    let cell = button.parentElement;
    let row = cell.parentElement;
    fetch("/products/delete/" + button.id).then((response) => {
        if (response.status == 200) {
            row.remove();
        }
    });
  }

  async function deleteProductAsync(event) {
    let button = event.target;
    let cell = button.parentElement;
    let row = cell.parentElement;
    let response = await fetch("/products/delete/" + button.id);
    if (response.status == 200) {
        row.remove();
    }
  }
