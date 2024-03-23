const SEARCH = {
  search: "",
  names: [
    "Simon",
    "Salmon",
    "Nganga",
    "Njoroge",
    "Faith",
    "Fish",
    "Omega",
    "Omena",
  ],
  get filtered() {
    return this.names.filter((name) =>
      name.toLowerCase().startsWith(this.search.toLowerCase())
    );
  },
  DIV1: {
    title: "This is DIV1"
  },
  DIV2: {
    title: "This is DIV2",
    swap1() {
      SEARCH.DIV1.title = "This is from DIV2"
      this.title = "Changed"
    }
  }
};
