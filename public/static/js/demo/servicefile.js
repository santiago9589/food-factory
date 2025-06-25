function deleteClient(clientId) {
    if (confirm("¿Estás seguro de que quieres eliminar este cliente?")) {
       
        fetch(`/client/delete-${clientId}`, {
            method: 'DELETE'
        })
        .then(response => {
            if (response.ok) {
                location.reload();
            } else {
                alert("Error al eliminar el cliente.");
            }
        });
    }
}




