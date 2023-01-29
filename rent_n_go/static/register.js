
var mealsByCategory = {
    Telangana: ["Select City", "Hyderabad", "Jagtial", "Siddipet", "Sirsicilla", "Gadwal"],
    Maharastra: ["Select City", "Mumbai", "pune", "Shiridi", "nashik"],
    Delhi: ["Select City", "Alipur", "Daryaganj", "Nand Nagri", "Saket", "Shivaji Palace"],
    AndhraPradesh: ["Select City", "Kurnool", "Vijayawada", "Nellore", "Thirupathi", "Kadapa"],
    Goa: ["Select City", "North Goa", "Panaji", "Madagaon", "South Goa"],
    Punjab: ["Select City", "Jalandhar", "Ludhiana", "Faridkot", "Gurdaspur"],
    ArunachalPradesh: ["Select City", "Changlang", "East Siang", "Upper Siang", "Tawang"],
    Kerala: ["Select City", "Thissur", "Kottayam", "Idukki", "Thrissur", "Kozhikkode"],
    Gujarat: ["Select City", "Gandhi Nagar", "Kheda", "Kachchh", "Surendranagar"],
    Karanata: ["Select City", "Bidar", "Shimoga", "Bellary", "Dakshina Kannada"],
    Assam: ["Select City", "Barpeta", "Dhubri", "Goalpara", "Darrang"],
    MadhyaPradesh: ["Select City", "Bhopal", "Jabalpur", "Indore", "Rajgarh"],


}

function changecat(value) {
    if (value.length == 0) document.getElementById("category").innerHTML = "<option></option>";
    else {
        var catOptions = "";
        for (categoryId in mealsByCategory[value]) {
            catOptions += "<option>" + mealsByCategory[value][categoryId] + "</option>";
        }
        document.getElementById("category").innerHTML = catOptions;
    }
}


const signUpAs = document.getElementById("signUpAs")

let hostEle = document.getElementById("host");
let customerEle = document.getElementById("customer");



function console() {
    console.log(hostEle.selected);
    console.log(hostEle);
    if (hostEle.selected) {
        console.log(hostEle.value);
    }
}
