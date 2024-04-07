import Header from './Header/Header.tsx';
import { Outlet } from 'react-router-dom';
import { ReactElement, useState } from 'react';
import { useSelectorTyped } from '../../hooks/store.ts';
import styled from 'styled-components';


const MainLayout = styled.main<{ $searchIsOpen: boolean }>`
  overflow: ${(props) => (props.$searchIsOpen ? 'hidden' : 'visible')};
`

function Layout(): ReactElement {


  const [navIsOpen, setNavIsOpen] = useState(false);
  const searchIsOpen = useSelectorTyped((store) => store.pageStatesReducer.searchIsOpen);

  function handleMenuOpen() {
    setNavIsOpen(!navIsOpen);
  }

  function handleMenuClose() {
    setTimeout(()=> setNavIsOpen(false), 300);
  }

  return (
    <>
      <Header handleMenuClose={handleMenuClose} handleMenuOpen={ handleMenuOpen } isMenuOpen={ navIsOpen }/>
      <MainLayout $searchIsOpen={searchIsOpen}>
        <Outlet/>
      </MainLayout>
    </>
  );
}

export default Layout;
