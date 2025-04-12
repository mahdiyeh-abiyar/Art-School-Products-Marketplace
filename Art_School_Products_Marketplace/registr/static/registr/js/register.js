const elements = {
    inputs: {
      name: document.querySelector(".name"),
      lastname: document.querySelector(".lastname"),
      phone: document.querySelector(".phone"),
      password: document.querySelector(".password"),
    },
    messages: {
      name: document.querySelector(".name-msg"),
      lastname: document.querySelector(".lastname-msg"),
      phone: document.querySelector(".phone-msg"),
      password: document.querySelector(".password-msg"),
      signin: document.querySelector(".signin-msg"),
    },
    button: document.querySelector(".signin-btn"),
  };
  
  const validationRules = {
    name: [
      { test: (value) => !!value, message: "لطفا نام خود را وارد کنید" },
      {
        test: (value) => value.length >= 2,
        message: "نام باید حداقل 2 حرف داشته باشد",
      },
      {
        test: (value) => /^[آ-یa-zA-Z\s]+$/.test(value),
        message: "نام فقط باید شامل حروف باشد",
      },
    ],
    lastname: [
      { test: (value) => !!value, message: "لطفا نام خانوادگی خود را وارد کنید" },
      {
        test: (value) => value.length >= 3,
        message: "نام خانوادگی باید حداقل 3 حرف داشته باشد",
      },
      {
        test: (value) => /^[آ-یa-zA-Z\s]+$/.test(value),
        message: "نام خانوادگی فقط باید شامل حروف باشد",
      },
    ],
    phone: [
      { test: (value) => !!value, message: "لطفا شماره تلفن خود را وارد کنید" },
      {
        test: (value) => /^09[0-9]{9}$/.test(value),
        message: "شماره تلفن باید با 09 شروع شود و 11 رقم باشد",
      },
    ],
    password: [
      { test: (value) => !!value, message: "لطفا رمز عبور خود را وارد کنید" },
      {
        test: (value) => value.length >= 8,
        message: "رمز عبور باید حداقل 8 کاراکتر داشته باشد",
      },
      {
        test: (value) => /[A-Z]/.test(value),
        message: "رمز عبور باید حداقل یک حرف بزرگ داشته باشد",
      },
      {
        test: (value) => /[0-9]/.test(value),
        message: "رمز عبور باید حداقل یک عدد داشته باشد",
      },
      {
        test: (value) => /[!@#$%^&*]/.test(value),
        message: "رمز عبور باید حداقل یک کاراکتر خاص داشته باشد",
      },
    ],
  };
  
  const resetValidation = () => {
    Object.values(elements.messages).forEach((msg) => {
      msg.textContent = "";
      msg.classList.remove("opacity-100", "text-red-500", "text-green-500");
      msg.classList.add("opacity-0");
    });
  
    Object.values(elements.inputs).forEach((input) => {
      input.classList.add("border-transparent");
    });
  };
  
  const showError = (field, message) => {
    elements.messages[field].textContent = message;
    elements.messages[field].classList.remove("opacity-0");
    elements.messages[field].classList.add("opacity-100", "text-red-500");
    elements.inputs[field].classList.remove("border-transparent");
  };
  
  const showSuccess = (message) => {
    elements.messages.signin.textContent = message;
    elements.messages.signin.classList.remove("opacity-0");
    elements.messages.signin.classList.add("opacity-100", "text-green-500");
  };
  
  const showServerError = (message) => {
    elements.messages.signin.textContent = message;
    elements.messages.signin.classList.remove("opacity-0");
    elements.messages.signin.classList.add("opacity-100", "text-red-500");
  };
  
  const validateField = (field, value) => {
    const rules = validationRules[field];
    for (const rule of rules) {
      if (!rule.test(value)) {
        return rule.message;
      }
    }
    return null;
  };
  
  const validateForm = (formData) => {
    let isValid = true;
  
    for (const [field, value] of Object.entries(formData)) {
      const errorMessage = validateField(field, value);
      if (errorMessage) {
        showError(field, errorMessage);
        isValid = false;
      }
    }
  
    return isValid;
  };
  
  const clearForm = () => {
    Object.values(elements.inputs).forEach((input) => {
      input.value = "";
    });
  };
  
  const submitForm = async (formData) => {
    try {
      const response = await fetch("https://jsonplaceholder.typicode.com/posts", {
        method: "POST",
        body: JSON.stringify(formData),
        headers: {
          "Content-Type": "application/json",
        },
      });
  
      if (response.ok) {
        showSuccess("ثبت نام شما با موفقیت انجام شد");
        clearForm();
      } else {
        throw new Error("Server response was not OK");
      }
    } catch (error) {
      showServerError("خطا در ارتباط با سرور");
      console.error("Error:", error);
    }
  };
  
  const handleSubmit = (event) => {
    event.preventDefault();
    resetValidation();
  
    const formData = {
      name: elements.inputs.name.value.trim(),
      lastname: elements.inputs.lastname.value.trim(),
      phone: elements.inputs.phone.value.trim(),
      password: elements.inputs.password.value.trim(),
    };
  
    if (validateForm(formData)) {
      submitForm(formData);
    }
  };
  
  elements.button.addEventListener("click", handleSubmit);
  