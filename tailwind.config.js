 /** @type {import('tailwindcss').Config} */
 export default {
  content: ['./templates/**/*.html',
    './**/templates/**/*.html'],
    safelist: [
      "bg-teal",
      "bg-Orange",
      "bg-white",
      "text-white",
      "text-grayblue",
      "rotate-90",
      "text-Orange"
    ],
  theme: {
    extend: {
      colors: {
        Orange: "#FE4F2D",
        "dark-teal": "#015551",
        teal: "#57B4BA",
        cream: "#FDFBEE",
        grayblue: "#9AA6B2",
        "darkgray": "#45474B",
        "light-gray": "#F5F7F8",
        "bright-orange": "#FF3B15",
      },
    },
  },
  plugins: [],
}