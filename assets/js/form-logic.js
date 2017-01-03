// function submitForm(form) {
// 		console.log("putas");

// 		var data = $(this).serializeArray().reduce(function(obj, item) {
// 			if (item.value == ""){	return; }
// 			obj[item.name] = item.value;
// 			return obj;
// 		}, {});

// 	}


$('#form').on('submit', function () {
	var data = [];
	data["name"] = $('#name').val();
	data["email"] = $('#email').val();
	data["msg"] = $('#message').val();
	jQuery.post("https://v1wesefrvk.execute-api.eu-central-1.amazonaws.com/prod/sendContactForm", data, "json");
	// jQuery.post("localhost:8000", data, "json");
})