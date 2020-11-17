import { createAppContainer } from 'react-navigation';
import { createStackNavigator } from 'react-navigation-stack';
import {createDrawerNavigator} from 'react-navigation-drawer';

import SplashScreen from "../features/SplashScreen";
import SideMenu from './sideMenu';
//@BlueprintImportInsertion
import BlankScreen014588Navigator from '../features/BlankScreen014588/navigator';
import BlankScreen114587Navigator from '../features/BlankScreen114587/navigator';
import BlankScreen014488Navigator from '../features/BlankScreen014488/navigator';

/**
 * new navigators can be imported here
 */

const AppNavigator = {

    //@BlueprintNavigationInsertion
BlankScreen014588: { screen: BlankScreen014588Navigator },
BlankScreen114587: { screen: BlankScreen114587Navigator },
BlankScreen014488: { screen: BlankScreen014488Navigator },

    /** new navigators can be added here */
    SplashScreen: {
      screen: SplashScreen
    }
};

const DrawerAppNavigator = createDrawerNavigator(
  {
    ...AppNavigator,
  },
  {
    contentComponent: SideMenu
  },
);

const AppContainer = createAppContainer(DrawerAppNavigator);

export default AppContainer;
