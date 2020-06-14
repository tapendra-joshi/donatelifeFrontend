const state = document.getElementById("state");
const city = document.getElementById("city");

window.addEventListener("load", () => {
	axios
		.get(`https://cors-anywhere.herokuapp.com/https://donate-life.herokuapp.com/blood_banks/states`)
		.then((res) => {
			res.data.data.forEach((el) => {
				state.insertAdjacentHTML("beforeend", `<option value="${el}">${el}</option>`);
			});
		})
		.catch((err) => {
			console.log(err);
		});
});

state.addEventListener("change", () => {
	axios
		.get(
			`https://cors-anywhere.herokuapp.com/https://donate-life.herokuapp.com/blood_banks/${
				state.options[state.selectedIndex].value
			}/cities`
		)
		.then((res) => {
			if (city.innerHTML === "") {
				res.data.data.forEach((el) => {
					city.insertAdjacentHTML("beforeend", `<option value="${el}">${el}</option>`);
				});
			} else {
				city.innerHTML = "";
				res.data.data.forEach((el) => {
					city.insertAdjacentHTML("beforeend", `<option value="${el}">${el}</option>`);
				});
			}
		})
		.catch((err) => {
			console.log(err);
		});
});
