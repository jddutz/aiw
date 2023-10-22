function showModalDialog(dialogId, targetUrl) {
  var modal = $('#' + dialogId);

  // Check if modal and submit button exist
  if (modal.length === 0) {
    console.error('Modal dialog, ' + dialogId + ', not found.');
    return;
  }

  var submitButton = $('#' + dialogId + 'Submit');

  // Check if modal and submit button exist
  if (modal.length === 0) {
    console.error('Modal dialog submit button, ' + dialogId + 'Submit, not found.');
    return;
  }

  // Update the dialog submit button's href to the target endpoint
  submitButton.attr('href', targetUrl);

  // Show the modal
  modal.modal('show');
}
