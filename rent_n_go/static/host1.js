var subjectObject = {
  "CAR": {
    Volkswagen: ["Polo", "Vento", "Virtus", "Taigun", "Tiguan"],
    Hyundai: ["i20", "Aura", "Grand i10 Nios", "Verna", "Alcazar"],
    Honda: ["City", "WR-V", "Amaze", "Verna", "Jazz"],
    Suzuki: ["Vitara Brezza", "Baleno", "Dzire", "Ertiga", "Celerio", "Alto K10", "Ciaz", "Ignis"],
    Renault: ["Triber", "Kwid", "Kiger", "Fluence"],
    Tata: ["Tigor", "Harrier", "Safari", "Nexon", "Indigo", "Punch", "Indica",],
    Ford: ["Ecosport", "Focus", "Fiesta", "Aspire", "Everest"],
    Toyota: ["Glanza", "Innova", "Hyryder", "Camry", "Fortuner"],
  },
  "BIKE": {
    TVS: ["Raider", "Apache", "Ntorq", "Ronin"],
    Hero: ["Splendor", "HF Deluxe", "Passion Pro", "Xpulse"],
    Honda: ["Activa 6G", "SP 125", "SHINE", "Unicorn", "Dio", "H'ness CB350"],
    RoyalEnfield: ["Super Meteor", "Classic 350", "Hunter 350", "Bullet", "Continental"],
    Bajaj: ["Pulsar NS200", "Dominar 400", "Platina 110", "Chetak"],
    Yamaha: ["MT 15 V2", "R15S", "FZS-F1 V3", "Areox"],
    Suzuki: ["Access 125", "Burgman Street", "Gixxer", "Avenis", "V-Strom SX"],
    JAWA: ["42 Bobber ", "Forty two", "42 2.1", "Perak"],
  }
}
window.onload = function () {
  var subjectSel = document.getElementById("subject");
  var topicSel = document.getElementById("topic");
  var chapterSel = document.getElementById("chapter");
  for (var x in subjectObject) {
    subjectSel.options[subjectSel.options.length] = new Option(x, x);
  }
  subjectSel.onchange = function () {
    //empty Chapters- and Topics- dropdowns
    chapterSel.length = 1;
    topicSel.length = 1;
    //display correct values
    for (var y in subjectObject[this.value]) {
      topicSel.options[topicSel.options.length] = new Option(y, y);
    }
  }
  topicSel.onchange = function () {
    //empty Chapters dropdown
    chapterSel.length = 1;
    //display correct values
    var z = subjectObject[subjectSel.value][this.value];
    for (var i = 0; i < z.length; i++) {
      chapterSel.options[chapterSel.options.length] = new Option(z[i], z[i]);
    }
  }
}