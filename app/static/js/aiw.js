function showModalDialog(dialogId, onSubmit, promptText="") {
  var modal = $('#' + dialogId);

  // Check if modal exists
  if (modal.length === 0) {
    console.error('Modal dialog, ' + dialogId + ', not found.');
    return;
  }

  console.debug('Showing modal dialog, ' + dialogId + '.');
  console.debug(promptText);

  if (promptText) {
    // Check if modal prompt text exists
    var modalPrompt = $('#' + dialogId + 'Prompt');

    if (modalPrompt.length === 0) {
      console.error('Element ID, #' + dialogId + 'Prompt, not found.');
    }
    else {
      modalPrompt.text(promptText);}
  }

  var form = $('#' + dialogId + 'Form');

  // Check if form exists
  if (form.length > 0) {
    console.debug('Setting form action to ' + onSubmit + '.');
    form.attr('action', onSubmit);
  }

  // Show the modal
  modal.modal('show');
}
