// js General

console.log("js general");

if(document.querySelector("#input-pdf")){
    const fileInput = document.querySelector('#input-pdf');
    fileInput.onchange = () => {
        if (fileInput.files.length > 0) {
            const fileName = document.querySelector('#display-pdf-title');
            fileName.textContent = fileInput.files[0].name;
            for (let i = 0; i < fileInput.files.length; i++) {
                if(i == 0){
                    fileName.title +=  fileInput.files[i].name;
                }else{
                    fileName.title +=  " / " + fileInput.files[i].name;
                }
            }
        }
    }
}
