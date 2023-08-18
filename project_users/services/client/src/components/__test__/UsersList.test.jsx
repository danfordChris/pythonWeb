import React from "react";
import renderer from "react-test-renderer";

import UsersList from "../UsersList";

const users = [
    {
        "active": true,
        "email": "hermanmu@gmail.com",
        "id": 1,
        "username": "michael"
    },
    {
        "active": true,
        "email": "michael@mherman.org",
        "id": 2,
        "username": "michaelherman"
    }
];

test("UsersList renders properly", () => {
    const component = renderer.create(<UsersList users={users} />);
    let tree = component.toJSON();
    expect(tree).toMatchSnapshot();
});

// Path: project_users\services\client\src\components\__test__\UsersList.test.jsx

test("UsersList renders a snapshot properly", () => {
    const tree = renderer.create(<UsersList users={users} />).toJSON();
    expect(tree).toMatchSnapshot();
}); 
