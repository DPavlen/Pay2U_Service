import { ReactElement } from 'react';
import './Header.scss';
import BurgerButton from './BurgerButton/BurgerButton.tsx';
import NavBurger from './NavBurger/NavBurger.tsx';
import styled from 'styled-components';
import { IconButton } from '@mui/material';
import backButtonIcon from '../../../images/icons_png/arrow-left.png';
import { Link, useLocation, useNavigate } from 'react-router-dom';

interface HeaderProps {
  handleMenuOpen: () => void;
  handleMenuClose: () => void;
  isMenuOpen: boolean;
}

const NavWrapper = styled.div<{ $backIsActive: boolean }>`
  display: flex;
  justify-content: ${({ $backIsActive }) =>
    $backIsActive ? 'space-between' : 'flex-end'};
  align-items: center;
  width: 100%;
`;

const BackButton = styled(IconButton)`
  height: 36px;
  & img {
    height: 24px;
  }
`;

function Header(props: HeaderProps): ReactElement {
  const location = useLocation();
  const navigate = useNavigate();
  const backIsActive = location.pathname !== '/' && location.pathname !== '/successful-purchase' && location.pathname !== '/onboarding';

  return (
    <header className="header">
      <NavWrapper $backIsActive={backIsActive}>
        {backIsActive && (
          <BackButton onClick={() => navigate(-1)}>
            <img src={backButtonIcon} alt="" />
          </BackButton>
        )}
        <BurgerButton
          handleMenuOpen={props.handleMenuOpen}
          isMenuOpen={props.isMenuOpen}
        />
      </NavWrapper>
      <NavBurger
        handleMenuClose={props.handleMenuClose}
        handleMenuOpen={props.handleMenuOpen}
        isMenuOpen={props.isMenuOpen}
      />
    </header>
  );
}

export default Header;
