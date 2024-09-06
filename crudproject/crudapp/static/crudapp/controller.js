$(document).ready(function() {
    // Add delete event listener for dynamically created delete buttons
    $('#bookList').on('click', '.delete-btn', function() {
        var bookId = $(this).data('id');
        deleteBook(bookId);
    });
});

// Delete a book function
function deleteBook(id) {
    $.ajax({
        url: `/delete/${id}/`,
        method: 'POST',
        success: function() {
            $(`#book-${id}`).remove();
        }
    });
}

// function editBook(id) {
//     window.location.href = `/update/${id}/`;  // Ensure the correct URL is used for editing
// }

