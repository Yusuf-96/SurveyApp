document.addEventListener("DOMContentLoaded", () => {
  const removeOption = () => {
    document.querySelectorAll(".remove-option").forEach((ele) => {
      ele.addEventListener("click", function () {
        this.parentNode.parentNode.removeChild(this.parentNode);
      });
    });
  };
  removeOption();

  const addOption = () => {
    document.querySelectorAll(".add-option").forEach((question) => {
      question.addEventListener("click", function () {
        let element = document.createElement("div");
        element.classList.add("choice");
        element.innerHTML = `<div class="flex items-baseline p-4"><input type="radio" id="" disabled>
          
            <input type="text"  class ="edit-choice focus:outline-none
                border-b-2 border-red-200
                w-full
                focus:border-red-600
                transition
                duration-700
                ease-out
                ml-4" name="choice" value="">
            <span class="remove-option" >&times;</span></div>`;
        document.querySelectorAll(".choices").forEach((choices) => {
          choices.insertBefore(
            element,
            choices.childNodes[choices.childNodes.length - 2]
          );
          removeOption();
        });
      });
    });
  };
  addOption();

  const deleteQuestion = () => {
    document.querySelectorAll(".delete-question").forEach((question) => {
      question.addEventListener("click", function () {
        document.querySelectorAll(".question").forEach((q) => {
          if (q.dataset.id === this.dataset.id) {
            q.parentNode.removeChild(q);
          }
        });
      });
    });
  };
  deleteQuestion();

  const addQuestion = () => {
    document.querySelector("#add-question").addEventListener("click", () => {
      let ele = document.createElement("div");
      ele.classList.add("margin-top-bottom");
      ele.classList.add("box");
      ele.classList.add("question-box");
      ele.classList.add("question");
      //  ele.setAttribute("data-id", result["question"].id);
      ele.innerHTML = ` <div
    class=" container
      max-w-7xl
      mx-auto
      bg-white
      rounded-xl
      shadow-md
      md:max-w-2xl
      mt-5
      lg:px-8
      sm:px-6
      border-l-4 border-red-500 margin-top-bottom box question-box question
    "
  >
    <div class="my-2 ">
      <div class="p-4">
        <div class="uppercase tracking-wide text-sm text-black font-semibold ">
          <input
            type="text"
            id="question"
            placeholder="Untitled Question"
            name="question"
            value=""
            class="
              
              focus:outline-none
              border-b-2 border-red-200
              block
              w-full
              focus:border-red-600
              transition
              duration-700
              py-2
              ease-out
            "
          />
        </div>
      </div>
      <div class="choices">
        <div class="choice flex items-baseline p-4">
          <input type="radio" value="choice" />
          <input
            type="text"
            id="choice"
            name="choice"
            value=""
            class="
              focus:outline-none
              border-b-2 border-red-200
              w-full
              focus:border-red-600
              transition
              duration-700
              ease-out
              ml-4
            "
            placeholder="option 1"
          />
          <span class="remove-option">&times;</span>
        </div>
        <div class="choice p-4 flex items-baseline">
          <input type="radio" id="add-choice" disabled />
          <input
            type="text"
            class="
              add-option
              focus:outline-none
              border-b-2 border-red-200
              w-full
              focus:border-red-600
              transition
              duration-700
              ease-out
              ml-4
            "
            placeholder="Add Option"
          />
        </div>
      </div>
      <div class="flex item-between justify-between p-4">
      <div><input type="checkbox" class="form-check" /> Required</div>
      <span class="delete-question">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-5 w-5"
          viewBox="0 0 20 20"
          fill="currentColor"
        >
          <path
            fill-rule="evenodd"
            d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z"
            clip-rule="evenodd"
          />
        </svg>
      </span>
    </div>
    </div>
  </div>
      `;
      document.querySelector(".container").appendChild(ele);
      addOption()
      deleteQuestion()
    });
  };
  addQuestion();
});
