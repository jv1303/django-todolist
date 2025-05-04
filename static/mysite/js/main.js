function confirmDelete(listUkey) {
    if (confirm("Are you sure you want to delete this list?")) {
        // Set the hidden input value
        document.getElementById('listToDelete').value = listUkey;
        // Submit the form
        document.getElementById('deleteForm').submit();
    }
    // If user cancels, do nothing
}