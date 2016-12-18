function submitForm(form) {
		console.log("putas");

		var data = $(this).serializeArray().reduce(function(obj, item) {
			if (item.value == ""){	return; }
			obj[item.name] = item.value;
			return obj;
		}, {});

	}