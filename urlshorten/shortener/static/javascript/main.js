function validateTextbox() 
{
	 var box = document.getElementById("usr");
	 var re=/http:\/\/127.0.0.1:8000\//;
	 if (re.test(box.value))
	 {
		 box.focus();
		 box.style.border = "solid 3px rgba(0,0,255,0.7)";
		 alert("Please enter a valid url.");
		 return false;
	 }

 }