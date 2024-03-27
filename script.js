/*addEventListener("DOMContentLoaded", () => {
  const imagenes = [
    "img/alcaravan.jpg",
    "img/bromelia.jpg",
    "img/colibri.jpg",
    "img/frailejon.jpeg",
    "img/condor-andes.jpg",
    "img/magnoliopsidas_boyaca.jpg",
    "img/oso de anteojos.jpg",
  ];

  let i = 1;
  const img1 = document.querySelector("#img1");
  const img2 = document.querySelector("#img2");
  const progressBar = document.querySelector("#progress-bar");
  const divIndicadores = document.querySelector("#indicadores");
  let porcentajeBase = 100 / imagenes.length; //Porcentaje total de la barra del progreso
  let porcentajeActual = porcentajeBase;

  for (let index = 0; index < imagenes.length; index++) {
    const div = document.createElement("div");
    div.classList.add("circles")
    div.id =index;
    divIndicadores.appendChild(div);
    
  }
});*/

function masInfoCundi() {
  let info = document.querySelector("#floraCundinamarca");
  let info2 = document.querySelector("#infoCundinamarca")
  
info.innerHTML = "Especies de flora y Fauna";
info2.innerHTML = "Cundinamarca es hogar de una impresionante diversidad de especies, incluyendo frailejones y bromelias en sus páramos, y cóndores que surcan los cielos de estas alturas. En los humedales de la sabana, se pueden encontrar tinguas y alcaravanes, mientras que las montañas neblinosas albergan osos de anteojos, dantas y venados. Además, las arenas blancas del río Magdalena son el hábitat de tortugas charapas y babillas. La región también se enorgullece de tener 87 tipos de orquídeas y 83 de colibríes, demostrando la riqueza natural de Cundinamarca."  
}

function menosInfoCundi() {
  let info = document.querySelector("#floraCundinamarca");
  info.innerHTML = ""; // Esto eliminará el contenido
  let info2 = document.querySelector("#infoCundinamarca")
  info2.innerHTML = "";
};

function masInfoBoyaca() {
  let info = document.querySelector("#floraBoyaca");
  let info2 = document.querySelector("#infoBoyaca")

info.innerHTML = "Especies de flora y Fauna de Boyacá";
info2.innerHTML = "Los ecosistemas de Boyacá, como los páramos y los bosques andinos, son hogares de especies emblemáticas como el frailejón y el oso andino. Además, Boyacá es un punto crucial para las aves migratorias, con 90 especies que visitan anualmente. Entre su flora, se destacan las plantas vasculares como las magnoliopsidas, con 3,131 especies, y las liliopsidas, con 868 especies. Además, cuenta con una notable variedad de musgos y helechos, como los polypodiopsidas, que suman 343 especies. En cuanto a la fauna, Boyacá alberga una amplia gama de vertebrados, incluyendo 105 especies de mamíferos y 1,163 especies de aves, muchas de las cuales son endémicas y migratorias. Los ecosistemas de páramo, bosque húmedo tropical, piedemonte llanero, y bosque andino y altoandino son cruciales para la supervivencia de estas especies."  
}

function menosInfoBoyaca() {
  let info = document.querySelector("#floraBoyaca");
  info.innerHTML = ""; // Esto eliminará el contenido
  let info2 = document.querySelector("#infoBoyaca")
  info2.innerHTML = "";
};