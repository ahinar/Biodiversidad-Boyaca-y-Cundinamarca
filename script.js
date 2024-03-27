addEventListener("DOMContentLoaded", () => {
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
});
