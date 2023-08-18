import React from "react";
import renderer from "react-test-renderer";

import AddUser from "../AddUser";

test("AddUser renders properly", () => {
    const component = renderer.create(<AddUser />);
    let tree = component.toJSON();
    expect(tree).toMatchSnapshot();
});