import styled from 'styled-components';
import { Button } from '@mui/material';
import { Link } from 'react-router-dom';
import SmallFullWidthCard from '../../components/SmallFullWidthCard/SmallFullWidthCard';
import folderIcon from '../../images/icons/folder.svg';
import walletIcon from '../../images/icons/wallet2.svg';
import crownIcon from '../../images/icons/crown.svg';
import iviPromo from '../../images/cards_images/ivi_promo.png';
import yandexPromo from '../../images/cards_images/yandex.plus_promo.png';

const Section = styled.section`
padding-bottom: 28px;
  display: flex;
  flex-direction: column;
  align-items: center;
  height: calc(100svh - 72px);
`;

const MainWrapper = styled.div`
  flex: 1 0 auto;
`;

const Title = styled.h1`
  align-self: flex-start;
  margin: 0;
  padding-block: 12px;
  text-align: left;
  font-weight: 600;
  line-height: 1.5;
`;
const CardList = styled.ul`
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  width: 100%;
  list-style: none;
  gap: 8px;
`;

const CardWrapper = styled.div`
  padding-block: 24px 40px;
  display: flex;
  gap: 15px;
  width: 100%;
`;
const PromoCard = styled.div`
  & img {
    border-radius: 12px;
    box-shadow: 0 4px 90px 0 rgba(95, 105, 131, 0.16),
      0 5px 4px 0 rgba(95, 105, 131, 0.08), 0 0 4px 0 rgba(95, 105, 131, 0.06);
    width: 100%;
  }
`;
const LinkWrapper = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  align-self: flex-end;
`;
const OnbordingLink = styled(Link)`
  display: block;
  margin-top: 20px;
  width: max-content;
  text-decoration: none;
  color: var(--navy-blue-2);
  &:active {
    color: var(--navy-blue-1);
  }
`;

export default function OnboardingPage() {
  return (
    <Section>
      <MainWrapper>
        <Title>Наш сервис умеет</Title>
        <CardList>
          <li>
            <SmallFullWidthCard
              card={{
                name: 'Хранить подписки в одном месте',
                icon: folderIcon,
              }}
            />
          </li>
          <li>
            <SmallFullWidthCard
              card={{
                name: 'Получать кэшбэк за каждую оплату',
                icon: walletIcon,
              }}
            />
          </li>
          <li>
            <SmallFullWidthCard
              card={{
                name: 'Управлять подписками в одном экране',
                icon: crownIcon,
              }}
            />
          </li>
        </CardList>
        <CardWrapper>
          <PromoCard>
            <img src={iviPromo} alt="" />
          </PromoCard>
          <PromoCard>
            <img src={yandexPromo} alt="" />
          </PromoCard>
        </CardWrapper>
      </MainWrapper>
      <LinkWrapper>
        <Button component={Link} to={'/guide'} variant="contained">Подробнее</Button>
        <OnbordingLink to={'/'}>Перейти на главный экран</OnbordingLink>
      </LinkWrapper>
    </Section>
  );
}
