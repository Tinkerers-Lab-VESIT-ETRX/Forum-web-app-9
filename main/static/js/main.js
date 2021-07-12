function handleReplyButton(discussionId) {
	const replyFormContainer = document.getElementById(`reply-form-container-${discussionId}`);
	 if (replyFormContainer) {
   		 replyFormContainer.className = 'reply-form-container enabled'
  	}
}

function handleCancelReply(discussionId) {
	 const replyFormContainer = document.getElementById(`reply-form-container-${discussionId}`);
	  if (replyFormContainer) {
    	replyFormContainer.className = 'reply-form-container'
  	}

}