function updateClient(clientId) {
    if (confirm("¿Estás seguro de que quieres editar el cliente?")) {
        // Redirige directamente en lugar de hacer fetch
        console.loh("entro")
        window.location.href = `/clients/update-${clientId}`;
    }
}
